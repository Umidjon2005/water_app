import 'package:flutter/material.dart';
import '../models/district.dart';

class DetailScreen extends StatelessWidget {
  final District district;

  const DetailScreen({super.key, required this.district});

  Color getStatusColor(String status) {
    if (status == "Yaxshi") return Colors.green;
    if (status == "Ortacha") return Colors.orange;
    return Colors.red;
  }

  Widget infoCard(String title, String value) {
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 6),
      child: ListTile(
        title: Text(title),
        subtitle: Text(value),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(district.name),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: getStatusColor(district.status).withOpacity(0.15),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Text(
                "Holat: ${district.status}",
                style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: getStatusColor(district.status),
                ),
              ),
            ),
            const SizedBox(height: 16),
            infoCard("pH", district.ph.toString()),
            infoCard("TDS", district.tds.toString()),
            infoCard("Turbidity", district.turbidity.toString()),
            infoCard("Chlorine", district.chlorine.toString()),
            const SizedBox(height: 16),
            const Text(
              "Suv uzilish ma'lumotlari",
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            infoCard("Boshlanish vaqti", district.outageStart),
            infoCard("Tugash vaqti", district.outageEnd),
            infoCard("Sabab", district.reason),
          ],
        ),
      ),
    );
  }
}