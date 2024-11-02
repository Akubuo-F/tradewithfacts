import 'package:flutter/material.dart';

class AppColor {
  static const Color darkThemePrimaryColor = Color(0xFF1E1E1E);
  static const Color darkThemeSecondaryColor = Color(0xFFFFA726);
  static const Color darkThemeBackgroundColor = Color(0xFF121212);
  static const Color darkThemeOtherColor = Color(0xFF2C2C2C);
  static const Color lightThemePrimaryColor = Color(0xFFFFFFFF);
  static const Color lightThemeSecondaryColor = Color(0xFF4CAF50);
  static const Color lightThemeBackgroundColor = Color(0xFFF5F5F5);
  static const Color lightThemeOtherColor = Color(0xFFFFD700);
  static const Color white = Colors.white;
  static const Color white24 = Colors.white24;
  static const Color white70 = Colors.white70;
  static const Color black = Colors.black;
  static const Color red = Colors.red;
  static const Color black87 = Colors.black87;
  static const Color black54 = Colors.black54;
}

class AppColorScheme {
  static const ColorScheme darkColorScheme = ColorScheme(
    brightness: Brightness.dark,
    primary: AppColor.darkThemePrimaryColor,
    onPrimary: AppColor.white,
    secondary: AppColor.darkThemeSecondaryColor,
    onSecondary: AppColor.black,
    error: AppColor.red,
    onError: AppColor.white,
    surface: AppColor.darkThemePrimaryColor,
    onSurface: AppColor.white,
  );
  static const ColorScheme lightColorScheme = ColorScheme(
      brightness: Brightness.light,
      primary: AppColor.lightThemePrimaryColor,
      onPrimary: AppColor.black,
      secondary: AppColor.lightThemeSecondaryColor,
      onSecondary: AppColor.white,
      error: AppColor.red,
      onError: AppColor.white,
      surface: AppColor.lightThemePrimaryColor,
      onSurface: AppColor.black);
}

class AppTextTheme {
  static const TextTheme darkTextTheme = TextTheme(
    displayLarge: TextStyle(
      color: AppColor.white,
      fontSize: 24,
      fontWeight: FontWeight.bold,
    ),
    titleLarge: TextStyle(
      color: AppColor.white,
      fontSize: 20,
      fontWeight: FontWeight.bold,
    ),
    bodyLarge: TextStyle(
      color: AppColor.white,
      fontSize: 16,
    ),
    bodyMedium: TextStyle(
      color: AppColor.white70,
      fontSize: 14,
    ),
  );
  static const TextTheme lightTextTheme = TextTheme(
    displayLarge: TextStyle(
      color: AppColor.black,
      fontSize: 24,
      fontWeight: FontWeight.bold,
    ),
    titleLarge: TextStyle(
      color: AppColor.black,
      fontSize: 20,
      fontWeight: FontWeight.bold,
    ),
    bodyLarge: TextStyle(
      color: AppColor.black87,
      fontSize: 16,
    ),
    bodyMedium: TextStyle(
      color: AppColor.black54,
      fontSize: 14,
    ),
  );
}

class AppButtonTheme {
  static const ButtonThemeData darkButtonTheme = ButtonThemeData(
    buttonColor: AppColor.darkThemeSecondaryColor,
    textTheme: ButtonTextTheme.primary,
  );
  static const ButtonThemeData lightButtonTheme = ButtonThemeData(
    buttonColor: AppColor.lightThemeSecondaryColor,
    textTheme: ButtonTextTheme.primary,
  );
}

class AppIconTheme {
  static const IconThemeData darkIconTheme = IconThemeData(
    color: AppColor.white,
  );
  static const IconThemeData lightIconTheme = IconThemeData(
    color: AppColor.black,
  );
}

class AppAppBarTheme {
  static AppBarTheme darkAppBarTheme = AppBarTheme(
    color: AppColor.darkThemePrimaryColor,
    iconTheme: AppIconTheme.darkIconTheme,
    titleTextStyle: AppTextTheme.darkTextTheme.titleLarge,
  );
  static AppBarTheme lightAppBarTheme = AppBarTheme(
    color: AppColor.lightThemePrimaryColor,
    iconTheme: AppIconTheme.lightIconTheme,
    titleTextStyle: AppTextTheme.lightTextTheme.titleLarge,
  );
}

class AppBottomNavigationTheme {
  static BottomNavigationBarThemeData darkBottomNavigationTheme =
      const BottomNavigationBarThemeData(
    backgroundColor: AppColor.darkThemePrimaryColor,
    selectedItemColor: AppColor.darkThemeSecondaryColor,
    unselectedItemColor: AppColor.white70,
  );
  static BottomNavigationBarThemeData lightBottomNavigationTheme =
      const BottomNavigationBarThemeData(
    backgroundColor: AppColor.lightThemePrimaryColor,
    selectedItemColor: AppColor.lightThemeSecondaryColor,
    unselectedItemColor: AppColor.black,
  );
}

class AppInputDecorationTheme {
  static InputDecorationTheme darkInputDecorationTheme = InputDecorationTheme(
    filled: true,
    fillColor: AppColor.darkThemeOtherColor,
    border: OutlineInputBorder(
      borderRadius: BorderRadius.circular(8.0),
      borderSide: BorderSide.none,
    ),
    hintStyle: AppTextTheme.darkTextTheme.bodyMedium,
  );
  static InputDecorationTheme lightInputDecorationTheme = InputDecorationTheme(
    filled: true,
    fillColor: AppColor.lightThemeOtherColor,
    border: OutlineInputBorder(
      borderRadius: BorderRadius.circular(8.0),
      borderSide: BorderSide.none,
    ),
    hintStyle: AppTextTheme.lightTextTheme.bodyMedium,
  );
}

class AppTheme {
  AppTheme._();

  static ThemeData darkTheme = ThemeData(
    colorScheme: AppColorScheme.darkColorScheme,
    scaffoldBackgroundColor: AppColor.darkThemeBackgroundColor,
    cardColor: AppColor.darkThemePrimaryColor,
    textTheme: AppTextTheme.darkTextTheme,
    buttonTheme: AppButtonTheme.darkButtonTheme,
    appBarTheme: AppAppBarTheme.darkAppBarTheme,
    inputDecorationTheme: AppInputDecorationTheme.darkInputDecorationTheme,
    iconTheme: AppIconTheme.darkIconTheme,
    bottomNavigationBarTheme:
        AppBottomNavigationTheme.darkBottomNavigationTheme,
    dividerColor: AppColor.white24,
  );
  static ThemeData lightTheme = ThemeData(
    colorScheme: AppColorScheme.lightColorScheme,
    scaffoldBackgroundColor: AppColor.lightThemeBackgroundColor,
    cardColor: AppColor.lightThemePrimaryColor,
    textTheme: AppTextTheme.lightTextTheme,
    buttonTheme: AppButtonTheme.lightButtonTheme,
    appBarTheme: AppAppBarTheme.lightAppBarTheme,
    inputDecorationTheme: AppInputDecorationTheme.lightInputDecorationTheme,
    iconTheme: AppIconTheme.lightIconTheme,
    bottomNavigationBarTheme:
        AppBottomNavigationTheme.lightBottomNavigationTheme,
    dividerColor: AppColor.black54,
  );
}
