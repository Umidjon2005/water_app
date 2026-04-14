import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/search_result.dart';

class LocationSearchService {
  static Future<List<SearchResult>> searchPlace(String query) async {
    final url = Uri.parse(
      'https://nominatim.openstreetmap.org/search?format=json&q=$query, Surxondaryo, Uzbekistan&limit=5',
    );

    final response = await http.get(
      url,
      headers: {
        'Accept': 'application/json',
      },
    );

    if (response.statusCode == 200) {
      final List data = jsonDecode(response.body);
      return data.map((e) => SearchResult.fromJson(e)).toList();
    } else {
      throw Exception("Qidiruvda xatolik: ${response.statusCode}");
    }
  }
}