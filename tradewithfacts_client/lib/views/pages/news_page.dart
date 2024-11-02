import 'package:flutter/material.dart';

class NewsPage extends StatelessWidget {
  const NewsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text(
        "News Page",
        style: Theme.of(context).textTheme.bodyLarge,
      ),
    );
  }
}
