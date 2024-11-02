import 'package:flutter/material.dart';

class FundamentalPage extends StatelessWidget {
  const FundamentalPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text(
        "Fundamental Page",
        style: Theme.of(context).textTheme.bodyLarge,
      ),
    );
  }
}
