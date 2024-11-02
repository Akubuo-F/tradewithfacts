import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:tradewithfacts_client/views/screens/home/providers/page_display_manager_provide.dart';

class PageDisplayManager extends StatelessWidget {
  const PageDisplayManager({super.key});

  @override
  Widget build(BuildContext context) {
    return SafeArea(
        child: context.watch<PageDisplayManagerProvider>().selectedPage);
  }
}
