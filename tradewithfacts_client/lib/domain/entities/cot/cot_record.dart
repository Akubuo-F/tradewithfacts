class COTRecord {
  final String assetName;
  final int long;
  final int short;
  final int changeInLong;
  final int changeInShort;
  final double longPercentage;
  final double shortPercentage;
  final double netPercentageChange;
  final int net;
  final int openInterest;
  final int changeInOpenInterest;

  COTRecord({
    required this.assetName,
    required this.long,
    required this.short,
    required this.changeInLong,
    required this.changeInShort,
    required this.longPercentage,
    required this.shortPercentage,
    required this.netPercentageChange,
    required this.net,
    required this.openInterest,
    required this.changeInOpenInterest,
  });
}