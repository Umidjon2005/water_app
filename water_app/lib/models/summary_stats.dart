class SummaryStats {
  final String region;
  final int latestYear;
  final double? latestCoveragePercent;
  final double? coverageGrowth;
  final double? totalWaterPipesKm;
  final double? sewerPipesKm;
  final int? waterFacilitiesCount;

  SummaryStats({
    required this.region,
    required this.latestYear,
    required this.latestCoveragePercent,
    required this.coverageGrowth,
    required this.totalWaterPipesKm,
    required this.sewerPipesKm,
    required this.waterFacilitiesCount,
  });

  factory SummaryStats.fromJson(Map<String, dynamic> json) {
    return SummaryStats(
      region: json['region'],
      latestYear: json['latest_year'],
      latestCoveragePercent: (json['latest_coverage_percent'] as num?)?.toDouble(),
      coverageGrowth: (json['coverage_growth'] as num?)?.toDouble(),
      totalWaterPipesKm: (json['total_water_pipes_km'] as num?)?.toDouble(),
      sewerPipesKm: (json['sewer_pipes_km'] as num?)?.toDouble(),
      waterFacilitiesCount: json['water_facilities_count'],
    );
  }
}