import 'package:flutter/material.dart';

class AppBottomNavigationBarProvider extends ChangeNotifier {
  int selectedItemIndex = 0;

  void navigateTo(int itemIndex) {
    selectedItemIndex = itemIndex;
    notifyListeners();
  }
}
