import 'package:flutter/material.dart';
import 'package:tradewithfacts_client/views/pages/fundamental_page.dart';
import 'package:tradewithfacts_client/views/pages/news_page.dart';
import 'package:tradewithfacts_client/views/pages/sentiment_page.dart';

class PageDisplayManagerProvider extends ChangeNotifier {
  Widget selectedPage = const SentimentPage();
  final List<Widget> _pagesToDisplay = [
    const SentimentPage(),
    const FundamentalPage(),
    const NewsPage(),
  ];

  void display(int pageIndex) {
    selectedPage = _pagesToDisplay[pageIndex];
    notifyListeners();
  }
}
