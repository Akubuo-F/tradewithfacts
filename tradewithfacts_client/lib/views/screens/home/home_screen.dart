import 'package:flutter/material.dart';
import 'package:tradewithfacts_client/views/screens/home/widgets/app_app_bar.dart';
import 'package:tradewithfacts_client/views/screens/home/widgets/app_bottom_navigation_bar.dart';
import 'package:tradewithfacts_client/views/screens/home/widgets/page_display_manager.dart';
import 'package:tradewithfacts_client/views/utils/responsive_manager.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: ResponsiveManager.isMobile(context)
          ? const AppAppBar().build(context)
          : null,
      body: const PageDisplayManager(),
      bottomNavigationBar: ResponsiveManager.isMobile(context)
          ? const AppBottomNavigationBar()
          : null,
    );
  }
}
