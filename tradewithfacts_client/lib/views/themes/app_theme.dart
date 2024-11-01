import 'package:flutter/material.dart';

class AppColors {
  static const Color primaryColor = Color(0xFF1C1C1E);
  static const Color secondaryColor = Color(0xFFFF9500);
  static const Color surfaceColor = Color(0xFF000000);
  static const Color onPrimary = Colors.white;
  static const Color onSecondary = Colors.black;
  static const Color onSurface = Colors.white;
}

class AppTheme {
  static final ThemeData darkTheme = ThemeData(
      brightness: Brightness.dark,
      primaryColor: AppColors.primaryColor,
      colorScheme: const ColorScheme.dark(
        primary: AppColors.primaryColor,
        secondary: AppColors.secondaryColor,
        surface: AppColors.surfaceColor,
        onPrimary: AppColors.onPrimary,
        onSecondary: AppColors.onSecondary,
        onSurface: AppColors.onSurface,
      ),
      textTheme: const TextTheme(
        headlineLarge: TextStyle(
          fontSize: 24,
          fontWeight: FontWeight.bold,
          color: AppColors.onPrimary,
        ),
        headlineMedium: TextStyle(
          fontSize: 20,
          fontWeight: FontWeight.bold,
          color: AppColors.onPrimary,
        ),
        headlineSmall: TextStyle(
          fontSize: 16,
          color: AppColors.onPrimary,
        ),
      ),
      buttonTheme: ButtonThemeData(
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(8.0),
        ),
        buttonColor: AppColors.secondaryColor,
        textTheme: ButtonTextTheme.primary,
      ),
      cardTheme: CardTheme(
          color: AppColors.primaryColor,
          margin: const EdgeInsets.all(8.0),
          shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(8.0))));
}
