import 'package:tradewithfacts_client/domain/entities/cot/cot_record.dart';

class COTReport {
  final String asOf;
  final String validTill;
  final List<COTRecord> records;

  COTReport({
    required this.asOf,
    required this.validTill,
    required this.records
  });
}