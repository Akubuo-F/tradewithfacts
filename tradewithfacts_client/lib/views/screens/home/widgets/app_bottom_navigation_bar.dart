import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:tradewithfacts_client/views/screens/home/providers/app_bottom_navigation_bar_provider.dart';
import 'package:tradewithfacts_client/views/screens/home/providers/page_display_manager_provide.dart';

class AppBottomNavigationBar extends StatelessWidget {
  const AppBottomNavigationBar({super.key});

  @override
  Widget build(BuildContext context) {
    return BottomNavigationBar(
      currentIndex:
          context.watch<AppBottomNavigationBarProvider>().selectedItemIndex,
      onTap: (selectedIndex) {
        context
            .read<AppBottomNavigationBarProvider>()
            .navigateTo(selectedIndex);
        context.read<PageDisplayManagerProvider>().display(selectedIndex);
      },
      items: _buildItems(),
    );
  }

  List<BottomNavigationBarItem> _buildItems() {
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
      (generatedIndex) => BottomNavigationBarItem(
        icon: icons[generatedIndex]!,
        label: labels[generatedIndex],
      ),
    );
  }
}
