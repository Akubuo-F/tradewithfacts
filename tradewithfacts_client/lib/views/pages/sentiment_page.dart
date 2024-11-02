import 'package:flutter/material.dart';

class SentimentPage extends StatelessWidget {
  const SentimentPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text(
        "Sentiment Page",
        style: Theme.of(context).textTheme.bodyLarge,
      ),
    );
  }
}
