import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:tradewithfacts_client/views/screens/home/home_screen.dart';
import 'package:tradewithfacts_client/views/screens/home/providers/app_bottom_navigation_bar_provider.dart';
import 'package:tradewithfacts_client/views/screens/home/providers/page_display_manager_provide.dart';
import 'package:tradewithfacts_client/views/themes/app_theme.dart';

void main() {
  runApp(MultiProvider(
    providers: [
      ChangeNotifierProvider(create: (_) => AppBottomNavigationBarProvider()),
      ChangeNotifierProvider(create: (_) => PageDisplayManagerProvider()),
    ],
    child: const App(),
  ));
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'TradeWithFacts',
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      themeMode: ThemeMode.system,
      home: const HomeScreen(),
    );
  }
}
