import 'package:http/http.dart' as http;
import "dart:convert";

import 'base/abstract_cot_repository.dart';

class COTRepository extends AbstractCOTRepository {
  final String _apiUrl = "http://127.0.0.1:8000/cot";

  @override
  Future<Map<String, dynamic>> fetchLatestReport() async {
    final response = await http.get(Uri.parse(_apiUrl));
    if (response.statusCode != 200) {
      throw Exception("Failed to load COT report.");
    }
    return json.decode(response.body);
  }
}


void main() async {
  COTRepository cotRepository = COTRepository();
  var data = await cotRepository.fetchLatestReport();
  print(data);
}