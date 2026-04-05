import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QStackedWidget, 
                             QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent

class PresentationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Türkiye'nin Ekonomik Faaliyetleri - Sunum")
        self.resize(1000, 700)
        self.setStyleSheet("background-color: #0b1220;")

        # Ana Widget ve Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Slayt Sayacı (Üst Sağ)
        self.counter_label = QLabel()
        self.counter_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.counter_label.setStyleSheet("""
            color: #e2e8f0; 
            font-size: 18px; 
            padding: 10px;
            background: rgba(255,255,255,0.08);
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.1);
        """)
        self.layout.addWidget(self.counter_label)

        # Slayt Alanı (Stacked Widget)
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Slayt İçerikleri
        self.slides_data = [
            {
                "title": "Türkiye'nin Ekonomik Faaliyetleri",
                "content": "Bu sunumda Türkiye'nin ekonomik faaliyetleri incelenecektir.\nEkonomi, ülkenin üretim, tüketim, ticaret ve hizmet alanlarını kapsar.",
                "subtext": "(İleri gitmek için butonları kullan veya klavyeden sağ/sol tuşlarını bas)"
            },
            {
                "title": "Ekonomik Faaliyet Nedir?",
                "content": "Ekonomik faaliyet, insanların ihtiyaçlarını karşılamak için yaptığı üretim ve hizmet çalışmalarının tamamıdır.",
                "list": ["• Tarım (toprak ürünleri)", "• Sanayi (fabrikalar, üretim)", "• Hizmet (turizm, ulaşım, eğitim)"]
            },
            {
                "title": "Türkiye'de Tarım Faaliyetleri",
                "content": "Türkiye’de tarım önemli bir ekonomik faaliyettir. İklim çeşitliliği sayesinde farklı ürünler yetişir.",
                "list": ["• Buğday, arpa (İç Anadolu)", "• Fındık (Karadeniz)", "• Zeytin (Ege)", "• Pamuk (Güneydoğu Anadolu)", "• Çay (Doğu Karadeniz)"]
            },
            {
                "title": "Hayvancılık",
                "content": "Hayvancılık tarımı destekleyen bir faaliyettir ve Türkiye'de yaygın olarak yapılır.",
                "list": ["• Büyükbaş hayvancılık (Marmara, Doğu Anadolu)", "• Küçükbaş hayvancılık (İç Anadolu, Güneydoğu)", "• Kümes hayvancılığı (Marmara)", "• Arıcılık (Karadeniz)"]
            },
            {
                "title": "Sanayi Faaliyetleri",
                "content": "Sanayi, ham maddelerin işlenip ürün haline getirilmesiyle oluşur.",
                "list": ["• Otomotiv (Bursa, Kocaeli)", "• Tekstil (İstanbul, Denizli, Gaziantep)", "• Demir-çelik (Karabük, İskenderun)", "• Gıda sanayi (Türkiye geneli)", "• Petrokimya (İzmir - Aliağa)"]
            },
            {
                "title": "Madencilik",
                "content": "Türkiye yer altı kaynakları bakımından zengindir. Madencilik sanayiyi destekler.",
                "list": ["• Bor minerali (Eskişehir, Balıkesir)", "• Kömür (Zonguldak)", "• Bakır (Artvin)", "• Krom (Elazığ)", "• Mermer (Afyon)"]
            },
            {
                "title": "Hizmet Sektörü",
                "content": "Hizmet sektörü günümüzde Türkiye ekonomisinin en büyük alanlarından biridir.",
                "list": ["• Ulaşım (kara, hava, deniz yolları)", "• Eğitim ve sağlık hizmetleri", "• Bankacılık ve finans", "• İletişim ve teknoloji", "• Turizm"]
            },
            {
                "title": "Turizm",
                "content": "Türkiye, doğal güzellikleri ve tarihi yapılarıyla turizmde güçlü bir ülkedir.",
                "list": ["• Antalya - yaz turizmi", "• İstanbul - kültür ve tarih turizmi", "• Kapadokya - doğal turizm", "• Trabzon - yayla turizmi", "• Pamukkale - sağlık turizmi"]
            },
            {
                "title": "Dış Ticaret",
                "content": "Türkiye hem ithalat hem ihracat yapan bir ülkedir. Dış ticaret ekonomiye büyük katkı sağlar.",
                "list": ["• İhraç edilen ürünler: otomotiv, tekstil, gıda", "• İthal edilen ürünler: enerji, teknoloji ürünleri", "• En önemli ticaret ortakları: Avrupa ülkeleri"]
            },
            {
                "title": "Sonuç",
                "content": "Türkiye’nin ekonomisi Tarım, Sanayi ve Hizmet sektörlerinden oluşur.\n\nBu faaliyetler ülkenin kalkınmasını sağlar ve halkın yaşam kalitesini artırır.",
                "subtext": "Sunum bitmiştir. Teşekkürler 🙌"
            }
        ]

        for data in self.slides_data:
            self.stacked_widget.addWidget(self.create_slide_widget(data))

        # Butonlar
        self.btn_layout = QHBoxLayout()
        self.prev_btn = QPushButton("⬅ Geri")
        self.next_btn = QPushButton("İleri ➡")

        button_style = """
            QPushButton {
                padding: 14px 30px;
                font-size: 18px;
                background-color: #2563eb;
                color: white;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #1d4ed8;
            }
        """
        self.prev_btn.setStyleSheet(button_style)
        self.next_btn.setStyleSheet(button_style)

        self.prev_btn.clicked.connect(self.prev_slide)
        self.next_btn.clicked.connect(self.next_slide)

        self.btn_layout.addStretch()
        self.btn_layout.addWidget(self.prev_btn)
        self.btn_layout.addWidget(self.next_btn)
        self.btn_layout.addStretch()
        self.layout.addLayout(self.btn_layout)

        # Alt Bilgi
        self.footer = QLabel("Türkiye Ekonomik Faaliyetler Sunumu")
        self.footer.setStyleSheet("color: rgba(255,255,255,0.6); font-size: 14px;")
        self.footer.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.footer)

        self.update_ui()

    def create_slide_widget(self, data):
        slide = QWidget()
        slide_layout = QVBoxLayout(slide)
        slide_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Başlık
        title = QLabel(data["title"])
        title.setWordWrap(True)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_color = "#38bdf8" if self.stacked_widget.count() == 0 else "#22c55e"
        title.setStyleSheet(f"color: {title_color}; font-size: 40px; font-weight: bold; margin-bottom: 10px;")
        slide_layout.addWidget(title)

        # İçerik Kutusu
        box = QFrame()
        box.setStyleSheet("""
            background: rgba(255,255,255,0.06);
            border-radius: 18px;
            border: 1px solid rgba(255,255,255,0.1);
            padding: 20px;
        """)
        box_layout = QVBoxLayout(box)

        content = QLabel(data["content"])
        content.setWordWrap(True)
        content.setStyleSheet("color: #e2e8f0; font-size: 22px; border: none;")
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        box_layout.addWidget(content)

        if "list" in data:
            list_text = "\n".join(data["list"])
            list_label = QLabel(list_text)
            list_label.setStyleSheet("color: #facc15; font-size: 20px; margin-top: 10px; border: none;")
            list_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            box_layout.addWidget(list_label)

        slide_layout.addWidget(box)

        if "subtext" in data:
            sub = QLabel(data["subtext"])
            sub.setStyleSheet("color: rgba(226, 232, 240, 0.7); font-size: 18px; margin-top: 10px;")
            sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
            slide_layout.addWidget(sub)

        return slide

    def update_ui(self):
        current = self.stacked_widget.currentIndex()
        total = self.stacked_widget.count()
        self.counter_label.setText(f"Slayt: {current + 1} / {total}")
        self.prev_btn.setEnabled(current > 0)
        self.next_btn.setEnabled(current < total - 1)

    def next_slide(self):
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() + 1)
        self.update_ui()

    def prev_slide(self):
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() - 1)
        self.update_ui()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Right:
            self.next_slide()
        elif event.key() == Qt.Key.Key_Left:
            self.prev_slide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PresentationApp()
    window.show()
    sys.exit(app.exec())