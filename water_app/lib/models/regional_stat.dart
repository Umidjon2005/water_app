class RegionalStat {
  final int id;
  final String regionName;
  final int year;
  final double? drinkingWaterCoveragePercent;
  final double? householdWaterCoveragePercent;
  final double? totalWaterPipesKm;
  final double? sewerPipesKm;
  final int? waterFacilitiesCount;
  final String? sourceNote;

  RegionalStat({
    required this.id,
    required this.regionName,
    required this.year,
    this.drinkingWaterCoveragePercent,
    this.householdWaterCoveragePercent,
    this.totalWaterPipesKm,
    this.sewerPipesKm,
    this.waterFacilitiesCount,
    this.sourceNote,
  });

  factory RegionalStat.fromJson(Map<String, dynamic> json) {
    return RegionalStat(
      id: json['id'],
      regionName: json['region_name'],
      year: json['year'],
      drinkingWaterCoveragePercent:
          json['drinking_water_coverage_percent'] != null
              ? (json['drinking_water_coverage_percent'] as num).toDouble()
              : null,
      householdWaterCoveragePercent:
          json['household_water_coverage_percent'] != null
              ? (json['household_water_coverage_percent'] as num).toDouble()
              : null,
      totalWaterPipesKm: json['total_water_pipes_km'] != null
          ? (json['total_water_pipes_km'] as num).toDouble()
          : null,
      sewerPipesKm: json['sewer_pipes_km'] != null
          ? (json['sewer_pipes_km'] as num).toDouble()
          : null,
      waterFacilitiesCount: json['water_facilities_count'],
      sourceNote: json['source_note'],
    );
  }
}