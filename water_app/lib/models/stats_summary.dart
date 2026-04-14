class StatsSummary {
  final String region;
  final int latestYear;
  final double? latestCoveragePercent;
  final double? coverageGrowth;
  final double? totalWaterPipesKm;
  final double? sewerPipesKm;
  final int? waterFacilitiesCount;

  StatsSummary({
    required this.region,
    required this.latestYear,
    this.latestCoveragePercent,
    this.coverageGrowth,
    this.totalWaterPipesKm,
    this.sewerPipesKm,
    this.waterFacilitiesCount,
  });

  factory StatsSummary.fromJson(Map<String, dynamic> json) {
    return StatsSummary(
      region: json['region'],
      latestYear: json['latest_year'],
      latestCoveragePercent: json['latest_coverage_percent'] != null
          ? (json['latest_coverage_percent'] as num).toDouble()
          : null,
      coverageGrowth: json['coverage_growth'] != null
          ? (json['coverage_growth'] as num).toDouble()
          : null,
      totalWaterPipesKm: json['total_water_pipes_km'] != null
          ? (json['total_water_pipes_km'] as num).toDouble()
          : null,
      sewerPipesKm: json['sewer_pipes_km'] != null
          ? (json['sewer_pipes_km'] as num).toDouble()
          : null,
      waterFacilitiesCount: json['water_facilities_count'],
    );
  }
}