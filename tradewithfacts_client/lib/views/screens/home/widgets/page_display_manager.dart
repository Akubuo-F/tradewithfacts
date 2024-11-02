import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:tradewithfacts_client/views/screens/home/providers/page_display_manager_provider.dart';
import 'package:tradewithfacts_client/views/screens/home/widgets/app_side_navigation_bar.dart';
import 'package:tradewithfacts_client/views/utils/responsive_manager.dart';

class PageDisplayManager extends StatelessWidget {
  const PageDisplayManager({super.key});

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Row(
        children: [
          if (!ResponsiveManager.isMobile(context))
            _displaySideNavigationBar(context),
          _displayPage(context),
        ],
      ),
    );
  }

  Widget _displaySideNavigationBar(BuildContext context) {
    return const Expanded(
      flex: 1,
      child: AppSideNavigationBar(),
    );
  }

  Widget _displayPage(BuildContext context) {
    return Expanded(
      flex: 6,
      child: context.watch<PageDisplayManagerProvider>().selectedPage,
    );
  }
}
