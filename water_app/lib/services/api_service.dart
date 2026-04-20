import 'dart:convert';
import 'package:http/http.dart' as http;
import 'api_config.dart';

class ApiService {

  // GET waters
  static Future<List<dynamic>> getWaters() async {
    final response = await http.get(
      Uri.parse("${ApiConfig.baseUrl}/water"),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception("Xatolik");
    }
  }

  // ADD water
  static Future<void> addWater(String name, String status) async {
    final response = await http.get(
      Uri.parse("${ApiConfig.baseUrl}/water/add?name=$name&status=$status"),
    );

    if (response.statusCode != 200) {
      throw Exception("Qo‘shishda xato");
    }
  }
}