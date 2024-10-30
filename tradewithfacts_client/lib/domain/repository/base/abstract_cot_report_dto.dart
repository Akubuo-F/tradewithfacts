import 'package:tradewithfacts_client/domain/entities/cot/cot_report.dart';

abstract class AbstractCOTReportDTO {
  COTReport fromJson (Map<String, dynamic> data);
}