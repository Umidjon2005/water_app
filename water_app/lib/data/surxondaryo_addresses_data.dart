class AddressPoint {
  final String title;
  final String district;
  final String type; // mahalla, kocha, bino
  final double lat;
  final double lng;
  final String note;

  const AddressPoint({
    required this.title,
    required this.district,
    required this.type,
    required this.lat,
    required this.lng,
    required this.note,
  });
}

const List<AddressPoint> surxondaryoAddresses = [
  AddressPoint(
    title: "Binafsha ko‘chasi",
    district: "Termiz",
    type: "kocha",
    lat: 37.2412,
    lng: 67.2832,
    note: "Termizdagi ko‘cha",
  ),
  AddressPoint(
    title: "Sahovat ko‘chasi",
    district: "Termiz",
    type: "kocha",
    lat: 37.2390,
    lng: 67.2860,
    note: "Termizdagi ko‘cha",
  ),
  AddressPoint(
    title: "Barkamol avlod ko‘chasi",
    district: "Termiz",
    type: "kocha",
    lat: 37.2440,
    lng: 67.2815,
    note: "Termizdagi ko‘cha",
  ),
  AddressPoint(
    title: "Islom Karimov ko‘chasi",
    district: "Termiz",
    type: "kocha",
    lat: 37.2430,
    lng: 67.2770,
    note: "Termizdagi ko‘cha",
  ),
  AddressPoint(
    title: "Saroymulkxonim ko‘chasi",
    district: "Termiz",
    type: "kocha",
    lat: 37.2360,
    lng: 67.2870,
    note: "Termizdagi ko‘cha",
  ),
  AddressPoint(
    title: "Axborot texnologiyalari fakulteti",
    district: "Termiz",
    type: "bino",
    lat: 37.2358,
    lng: 67.2798,
    note: "Sport majmuasi yonidagi bino uchun custom label",
  ),
  AddressPoint(
    title: "Markaz mahallasi",
    district: "Angor",
    type: "mahalla",
    lat: 37.4711,
    lng: 67.0564,
    note: "Angor tumanidagi mahalla",
  ),
  AddressPoint(
    title: "Yangiobod mahallasi",
    district: "Jarqo‘rg‘on",
    type: "mahalla",
    lat: 37.5036,
    lng: 67.4158,
    note: "Jarqo‘rg‘on hududidagi mahalla",
  ),
  AddressPoint(
    title: "O‘zbekiston ko‘chasi",
    district: "Jarqo‘rg‘on",
    type: "kocha",
    lat: 37.5050,
    lng: 67.4170,
    note: "Jarqo‘rg‘on markaziy ko‘chasi",
  ),
  AddressPoint(
    title: "Paxtazavod mahallasi",
    district: "Jarqo‘rg‘on",
    type: "mahalla",
    lat: 37.5060,
    lng: 67.4200,
    note: "Rasmiy hujjatlarda uchragan mahalla",
  ),
  AddressPoint(
    title: "M. Utanov ko‘chasi",
    district: "Jarqo‘rg‘on",
    type: "kocha",
    lat: 37.5065,
    lng: 67.4215,
    note: "Rasmiy hujjatlarda uchragan ko‘cha",
  ),
];