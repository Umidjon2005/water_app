class MapLocation {
  final String name;
  final String district;
  final double lat;
  final double lng;
  final String description;
  final String stats;
  final String status;

  const MapLocation({
    required this.name,
    required this.district,
    required this.lat,
    required this.lng,
    required this.description,
    required this.stats,
    required this.status,
  });
}