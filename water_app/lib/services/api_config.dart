import 'package:flutter/foundation.dart';

class ApiConfig {
  static String get baseUrl {
    if (kIsWeb) {
      return 'http://10.26.2.78';
    }
    return 'http://10.26.2.78';
  }
}
