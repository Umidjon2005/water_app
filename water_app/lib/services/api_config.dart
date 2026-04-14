import 'package:flutter/foundation.dart';

class ApiConfig {
  static String get baseUrl {
    if (kIsWeb) {
      return 'http://192.168.1.7:8000';
    }
    return 'http://192.168.1.7:8000';
  }
}