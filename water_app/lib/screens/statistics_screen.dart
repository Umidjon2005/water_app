import 'package:flutter/material.dart';
import '../models/regional_stat.dart';
import '../models/stats_summary.dart';
import '../services/api_service.dart';

class StatisticsScreen extends StatelessWidget {
  final bool isDarkMode;
  final VoidCallback onToggleTheme;

  const StatisticsScreen({
    super.key,
    required this.isDarkMode,
    required this.onToggleTheme,
  });

  Widget statCard({
    required String title,
    required String value,
    required IconData icon,
  }) {
    return Card(
      child: ListTile(
        leading: Icon(icon),
        title: Text(title),
        subtitle: Text(
          value,
          style: const TextStyle(
            fontSize: 18,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
    );
  }

  String formatDouble(double? value, {String suffix = ""}) {
    if (value == null) return "-";
    return "${value.toStringAsFixed(1)}$suffix";
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Statistika"),
        actions: [
          IconButton(
            onPressed: onToggleTheme,
            icon: Icon(isDarkMode ? Icons.light_mode : Icons.dark_mode),
          ),
        ],
      ),
      body: FutureBuilder<List<dynamic>>(
        future: Future.wait([
          ApiService.fetchSurxondaryoSummary(),
          ApiService.fetchSurxondaryoStats(),
        ]),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(
              child: CircularProgressIndicator(),
            );
          }

          if (snapshot.hasError) {
            return Center(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Text(
                  "Xatolik: ${snapshot.error}",
                  textAlign: TextAlign.center,
                ),
              ),
            );
          }

          final summary = snapshot.data![0] as StatsSummary;
          final stats = snapshot.data![1] as List<RegionalStat>;

          return SingleChildScrollView(
            padding: const EdgeInsets.all(12),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  "${summary.region} bo‘yicha umumiy ko‘rsatkichlar",
                  style: const TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 12),
                statCard(
                  title: "Oxirgi yil",
                  value: summary.latestYear.toString(),
                  icon: Icons.calendar_today,
                ),
                statCard(
                  title: "Ichimlik suvi qamrovi",
                  value: formatDouble(
                    summary.latestCoveragePercent,
                    suffix: "%",
                  ),
                  icon: Icons.water_drop,
                ),
                statCard(
                  title: "O‘sish",
                  value: formatDouble(
                    summary.coverageGrowth,
                    suffix: "%",
                  ),
                  icon: Icons.trending_up,
                ),
                statCard(
                  title: "Quvur uzunligi",
                  value: formatDouble(
                    summary.totalWaterPipesKm,
                    suffix: " km",
                  ),
                  icon: Icons.linear_scale,
                ),
                statCard(
                  title: "Kanalizatsiya tarmog‘i",
                  value: formatDouble(
                    summary.sewerPipesKm,
                    suffix: " km",
                  ),
                  icon: Icons.route,
                ),
                statCard(
                  title: "Suv inshootlari soni",
                  value: summary.waterFacilitiesCount?.toString() ?? "-",
                  icon: Icons.apartment,
                ),
                const SizedBox(height: 20),
                const Text(
                  "Yillar kesimida statistika",
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 10),
                ...stats.map((item) {
                  return Card(
                    child: ListTile(
                      title: Text("${item.year}"),
                      subtitle: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            "Qamrov: ${formatDouble(item.drinkingWaterCoveragePercent, suffix: "%")}",
                          ),
                          Text(
                            "Quvur: ${formatDouble(item.totalWaterPipesKm, suffix: " km")}",
                          ),
                          Text(
                            "Kanalizatsiya: ${formatDouble(item.sewerPipesKm, suffix: " km")}",
                          ),
                          Text(
                            "Inshootlar: ${item.waterFacilitiesCount?.toString() ?? "-"}",
                          ),
                          if (item.sourceNote != null)
                            Text("Izoh: ${item.sourceNote}"),
                        ],
                      ),
                    ),
                  );
                }),
              ],
            ),
          );
        },
      ),
    );
  }
}