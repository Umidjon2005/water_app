class District {
  final int id;
  final String name;
  final double ph;
  final int tds;
  final double turbidity;
  final double chlorine;
  final String status;
  final String outageStart;
  final String outageEnd;
  final String reason;

  District({
    required this.id,
    required this.name,
    required this.ph,
    required this.tds,
    required this.turbidity,
    required this.chlorine,
    required this.status,
    required this.outageStart,
    required this.outageEnd,
    required this.reason,
  });

  factory District.fromJson(Map<String, dynamic> json) {
    return District(
      id: json['id'],
      name: json['name'],
      ph: (json['ph'] as num).toDouble(),
      tds: json['tds'],
      turbidity: (json['turbidity'] as num).toDouble(),
      chlorine: (json['chlorine'] as num).toDouble(),
      status: json['status'],
      outageStart: json['outage_start'],
      outageEnd: json['outage_end'],
      reason: json['reason'],
    );
  }
}