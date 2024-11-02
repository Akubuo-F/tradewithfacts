import 'package:flutter/material.dart';

class ResponsiveManager {
  static const RangeValues _mobile = RangeValues(0, 599);
  static const RangeValues _tablet = RangeValues(600, 1023);
  static const RangeValues _desktop = RangeValues(1024, double.infinity);

  ResponsiveManager._();

  static bool isMobile(BuildContext context) {
    return _mobile.start <= MediaQuery.sizeOf(context).width &&
        MediaQuery.sizeOf(context).width <= _mobile.end;
  }

  static bool isTablet(BuildContext context) {
    return _tablet.start <= MediaQuery.sizeOf(context).width &&
        MediaQuery.sizeOf(context).width <= _tablet.end;
  }

  static bool isDesktop(BuildContext context) {
    return _desktop.start <= MediaQuery.sizeOf(context).width &&
        MediaQuery.sizeOf(context).width <= _desktop.end;
  }
}
