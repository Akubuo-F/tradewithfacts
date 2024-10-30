import 'package:tradewithfacts_client/domain/repository/base/abstract_cot_repository.dart';
import 'package:tradewithfacts_client/domain/repository/latest_report_fetcher.dart';


void main() {
  AbstractCOTRepository cotRepository = COTRepository();
  TestAbstractCOTRepository test = TestAbstractCOTRepository(cotRepository: cotRepository);
  test.testFetchLatestReport();
}


class TestAbstractCOTRepository {
  final AbstractCOTRepository cotRepository;

  TestAbstractCOTRepository({required this.cotRepository});

  void testFetchLatestReport() async {
    Map<String, dynamic> expected = {
      "message": {
        "as_of": "2024-10-22",
        "valid_till": "2024-11-01",
        "records": [
          {
            "asset": {
              "code": "XPT",
              "name": "PLATINUM",
              "asset_type": "COMMODITY"
            },
            "speculators": {
              "long": 53816,
              "short": 18940,
              "change_in_long": 7293,
              "change_in_short": 804
            },
            "hedgers": {
              "long": 13877,
              "short": 54612,
              "change_in_long": -294,
              "change_in_short": 5902
            },
            "open_interest": 81497,
            "change_in_open_interest": 8530
          },
          {
            "asset": {
              "code": "AUD",
              "name": "AUSTRALIAN DOLLAR",
              "asset_type": "CURRENCY"
            },
            "speculators": {
              "long": 102509,
              "short": 74830,
              "change_in_long": 3458,
              "change_in_short": -4952
            },
            "hedgers": {
              "long": 51825,
              "short": 9365,
              "change_in_long": -4577,
              "change_in_short": -1125
            },
            "open_interest": 186950,
            "change_in_open_interest": -6339
          },
          {
            "asset": {
              "code": "NDX",
              "name": "NASDAQ-100",
              "asset_type": "INDEX"
            },
            "speculators": {
              "long": 48989,
              "short": 46329,
              "change_in_long": 146,
              "change_in_short": -1110
            },
            "hedgers": {
              "long": 149502,
              "short": 162624,
              "change_in_long": 1187,
              "change_in_short": 1900
            },
            "open_interest": 245897,
            "change_in_open_interest": 4706
          }
        ]
      }
    };

    var result = await cotRepository.fetchLatestReport();

    if (expected == result) {
      throw Exception("expected != result. Test Failed!");
    }
    print("Result: $result");
    print("Test Passed!");
  }
}