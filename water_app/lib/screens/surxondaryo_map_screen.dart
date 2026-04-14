import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong.dart';
import 'package:url_launcher/url_launcher.dart';

import '../data/surxondaryo_map_data.dart';
import '../models/map_location.dart';

class SurxondaryoMapScreen extends StatelessWidget {
  final bool isDarkMode;
  final VoidCallback onToggleTheme;

  const SurxondaryoMapScreen({
    super.key,
    required this.isDarkMode,
    required this.onToggleTheme,
  });

  Color _getMarkerColor(String status) {
    switch (status) {
      case "yaxshi":
        return Colors.green;
      case "ortacha":
        return Colors.orange;
      case "yomon":
        return Colors.red;
      default:
        return Colors.blue;
    }
  }

  Future<void> _openInGoogleMaps(double lat, double lng) async {
    final uri = Uri.parse(
      'https://www.google.com/maps/search/?api=1&query=$lat,$lng',
    );

    if (!await launchUrl(uri, mode: LaunchMode.externalApplication)) {
      throw Exception("Google Maps ochilmadi");
    }
  }

  void _showLocationInfo(BuildContext context, MapLocation location) {
    showModalBottomSheet(
      context: context,
      showDragHandle: true,
      builder: (_) => Padding(
        padding: const EdgeInsets.all(16),
        child: Wrap(
          children: [
            Text(
              location.name,
              style: const TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            Text("Tuman: ${location.district}"),
            const SizedBox(height: 8),
            Text(location.description),
            const SizedBox(height: 12),
            Text("Statistika: ${location.stats}"),
            const SizedBox(height: 12),
            Row(
              children: [
                const Text("Holati: "),
                Text(
                  location.status,
                  style: TextStyle(
                    color: _getMarkerColor(location.status),
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            ElevatedButton.icon(
              onPressed: () => _openInGoogleMaps(location.lat, location.lng),
              icon: const Icon(Icons.map),
              label: const Text("Google Maps’da ochish"),
            ),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final tileUrl = isDarkMode
        ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
        : 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';

    final markers = surxondaryoMapLocations.map((location) {
      return Marker(
        point: LatLng(location.lat, location.lng),
        width: 44,
        height: 44,
        child: GestureDetector(
          onTap: () => _showLocationInfo(context, location),
          child: Icon(
            Icons.location_on,
            size: 38,
            color: _getMarkerColor(location.status),
          ),
        ),
      );
    }).toList();

    return Scaffold(
      appBar: AppBar(
        title: const Text("Surxondaryo suv xaritasi"),
        actions: [
          IconButton(
            onPressed: onToggleTheme,
            icon: Icon(isDarkMode ? Icons.light_mode : Icons.dark_mode),
          ),
        ],
      ),
      body: FlutterMap(
        options: const MapOptions(
          initialCenter: LatLng(37.9, 67.4),
          initialZoom: 8,
        ),
        children: [
          TileLayer(
            urlTemplate: tileUrl,
            subdomains: const ['a', 'b', 'c'],
            userAgentPackageName: 'com.example.water_app',
          ),
          MarkerLayer(markers: markers),
        ],
      ),
    );
  }
}