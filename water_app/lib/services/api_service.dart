import 'dart:convert';
import 'package:http/http.dart' as http;

import '../models/district.dart';
import '../models/regional_stat.dart';
import '../models/stats_summary.dart';
import 'api_config.dart';

class ApiService {
  static String get baseUrl => ApiConfig.baseUrl;

  static Future<List<District>> fetchDistricts() async {
    final response = await http.get(Uri.parse('$baseUrl/districts'));

    if (response.statusCode == 200) {
      final List data = jsonDecode(response.body);
      return data.map((e) => District.fromJson(e)).toList();
    } else {
      throw Exception('Server xatosi: ${response.statusCode}');
    }
  }

  static Future<List<RegionalStat>> fetchSurxondaryoStats() async {
    final response = await http.get(Uri.parse('$baseUrl/stats/surxondaryo'));

    if (response.statusCode == 200) {
      final List data = jsonDecode(response.body);
      return data.map((e) => RegionalStat.fromJson(e)).toList();
    } else {
      throw Exception('Statistika xatosi: ${response.statusCode}');
    }
  }

  static Future<StatsSummary> fetchSurxondaryoSummary() async {
    final response =
        await http.get(Uri.parse('$baseUrl/stats/surxondaryo/summary'));

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return StatsSummary.fromJson(data);
    } else {
      throw Exception('Summary xatosi: ${response.statusCode}');
    }
  }
}