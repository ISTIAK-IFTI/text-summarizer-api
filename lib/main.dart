import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(SummarizerApp());
}

class SummarizerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Text Summarizer',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: SummarizerHomePage(),
    );
  }
}

class SummarizerHomePage extends StatefulWidget {
  @override
  _SummarizerHomePageState createState() => _SummarizerHomePageState();
}

class _SummarizerHomePageState extends State<SummarizerHomePage> {
  final TextEditingController _textController = TextEditingController();
  String _summary = "";
  bool _isLoading = false;

  Future<void> _summarizeText() async {
    setState(() {
      _isLoading = true;
      _summary = "";
    });

    final url = Uri.parse("http://localhost:8000/summarize"); // Change if on real device

    // final url = Uri.parse("https://text-summarizer-api-fxff.onrender.com/summarize");


    try {
      final response = await http.post(
        url,
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"text": _textController.text}),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        setState(() {
          _summary = data["summary"];
        });
      } else {
        setState(() {
          _summary = "Error: ${response.statusCode}";
        });
      }
    } catch (e) {
      setState(() {
        _summary = "Failed to connect to server.";
      });
    }

    setState(() {
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Text Summarizer"),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _textController,
              maxLines: 8,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                labelText: "Enter text to summarize",
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _isLoading ? null : _summarizeText,
              child: Text("Summarize"),
            ),
            SizedBox(height: 20),
            _isLoading
                ? CircularProgressIndicator()
                : Text(
              _summary.isEmpty ? "Summary will appear here" : _summary,
              style: TextStyle(fontSize: 16),
            ),
          ],
        ),
      ),
    );
  }
}
