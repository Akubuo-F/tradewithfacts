import 'package:tradewithfacts_client/domain/entities/cot/cot_record.dart';
import 'package:tradewithfacts_client/domain/entities/cot/cot_report.dart';

import 'base/abstract_cot_report_dto.dart';

class COTReportDTO extends AbstractCOTReportDTO {

  @override
  COTReport fromJson(Map<String, dynamic> data) {
    String asOf = data["message"]["as_of"];
    String validTill = data["message"]["valid_till"];
    List<COTRecord> records = [];
    for (Map<String, dynamic> record in data["message"]["records"]) {
      int long = record["speculators"]["long"];
      int short = record["speculators"]["short"];
      COTRecord cotRecord = COTRecord(
        assetName: record["asset"]["name"],
        long : long,
        short : short,
        changeInLong : record["speculators"]["change_in_long"],
        changeInShort : record["speculators"]["change_in_short"],
        longPercentage : (long / (long + short)) * 100,
        shortPercentage : (short / (long + short)) * 100,
        netPercentageChange : .0,
        net : long - short,
        openInterest : record["asset"]["open_interest"],
        changeInOpenInterest : record["asset"]["change_in_open_interest"]
      );
      records.add(cotRecord);
    }
    return COTReport(
        asOf: asOf,
        validTill: validTill,
        records: records
    );
  }
}