import 'package:flutter/material.dart';

class AppAppBar extends StatelessWidget {
  const AppAppBar({super.key});

  @override
  AppBar build(BuildContext context) {
    return AppBar(
      centerTitle: true,
      title: Text(
        "TradeWithFacts",
        style: Theme.of(context).textTheme.titleLarge,
      ),
      actions: _buildActions(context),
    );
  }

  List<Widget> _buildActions(BuildContext context) {
    return [
      Padding(
        padding: const EdgeInsets.all(8.0),
        child: IconButton(
          onPressed: () {},
          icon: const Icon(Icons.notifications),
        ),
      ),
    ];
  }
}
