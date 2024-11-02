import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:tradewithfacts_client/views/screens/home/providers/app_navigation_bar_provider.dart';
import 'package:tradewithfacts_client/views/screens/home/providers/page_display_manager_provider.dart';
import 'package:tradewithfacts_client/views/utils/responsive_manager.dart';

class AppSideNavigationBar extends StatelessWidget {
  const AppSideNavigationBar({super.key});

  @override
  Widget build(BuildContext context) {
    return NavigationRail(
      selectedIndex:
          context.watch<AppNavigationBarProvider>().selectedItemIndex,
      onDestinationSelected: (selectedIndex) {
        context.read<AppNavigationBarProvider>().navigateTo(selectedIndex);
        context.read<PageDisplayManagerProvider>().display(selectedIndex);
      },
      extended: ResponsiveManager.isDesktop(context),
      selectedIconTheme: Theme.of(context).iconTheme,
      selectedLabelTextStyle:
          TextStyle(color: Theme.of(context).colorScheme.secondary),
      destinations: _buildDestinations(context),
    );
  }

  List<NavigationRailDestination> _buildDestinations(BuildContext context) {
    Map<int, Icon> icons = {
      0: const Icon(Icons.sentiment_very_satisfied),
      1: const Icon(Icons.public_rounded),
      2: const Icon(Icons.newspaper),
    };
    Map<int, String> labels = {
      0: "Sentiment",
      1: "Fundamental",
      2: "News",
    };
    if (icons.length != labels.length) {
      throw Exception("icons and labels must have the same length.");
    }
    return List.generate(
      icons.length,
      (generatedIndex) => NavigationRailDestination(
        icon: icons[generatedIndex]!,
        label: Text(labels[generatedIndex]!),
      ),
    );
  }
}
