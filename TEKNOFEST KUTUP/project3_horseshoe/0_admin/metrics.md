# Performans ve Metrik Raporu (Horseshoe Island)

| Modül | Ölçüt / Metrik | Beklenen/Hedef Değer | Elde Edilen Değer | Notlar |
| :--- | :--- | :---: | :---: | :--- |
| **A) DEM FaultSeg** | IoU (Intersection over Union) | > %75 | *hesaplanacak* | Yüksek çözünürlüklü fay izi örtüşmesi |
| | Boundary-F1 | > %80 | *hesaplanacak* | Sarplık çizgisine 100m tolerans mesafesi |
| | Completeness (Recall) | > %85 | *hesaplanacak* | Referans fayı kaçırmama oranı |
| **B) InSAR Zaman Serisi** | Geçerli Piksel Oranı | > %40 | *hesaplanacak* | Koherens maskesi sonrası kalan alan |
| | Hız Belirsizliği (Ortalama) | < 2 mm/yıl | *hesaplanacak* | Zaman serisi lineer fit hatası |
| | Fay Yakını LOS Gradyanı | İstatistiksel Anlamlı | *hesaplanacak* | Fay tampon bölgesinde gerinim birikimi |
| **C) Sismik Sınıflayıcı** | ROC-AUC (Glacial vs Tectonic)| > 0.85 | *hesaplanacak* | Spektrogram tabanlı ML performansı |
| | Macro-F1 Skor | > 0.80 | *hesaplanacak* | Sınıf dengesizliği altında başarı |
| **D) Risk Füzyon Endeksi** | Ablation Sıralama Kararlılığı | Spearman ρ > 0.80| *hesaplanacak* | Veri çıkarıldığında en riskli 10 fay değişiyor mu? |