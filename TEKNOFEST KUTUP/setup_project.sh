#!/bin/bash
# setup_project.sh - Horseshoe Island Projesi Klasör ve Altyapı Kurulum Betiği

echo "🚀 Proje-3: Horseshoe Island Sanal Paleosismoloji altyapısı kuruluyor..."

# Ana klasörler
mkdir -p project3_horseshoe/{0_admin,1_data_raw,2_data_intermediate,3_models,4_outputs,5_validation,6_repro,scripts}

cd project3_horseshoe

# Alt klasörler (Veri)
mkdir -p 1_data_raw/{dem_rema,s1_slc,s1_orbits,seismic_catalogs,seismic_waveforms,gia_models,aux_optical_s2}
mkdir -p 2_data_intermediate/{dem_tiles,dem_derivatives,faults_labels_weak,insar_stack,insar_timeseries,seismic_features}

# Alt klasörler (Çıktı ve Validasyon)
mkdir -p 4_outputs/{maps,figures,tables,uncertainty}
mkdir -p 5_validation/{manual_qc_samples,cross_sections,ablation_studies}
mkdir -p 6_repro/{docker,configs}

# Boş dosyaları oluştur
touch 0_admin/problem_spec.md
touch 0_admin/metrics.md
touch 0_admin/citations.bib
touch 6_repro/configs/config.yaml

echo "✅ Klasör ağacı başarıyla oluşturuldu!"