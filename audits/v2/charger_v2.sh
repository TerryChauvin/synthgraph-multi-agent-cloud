#!/bin/bash
# Contrôle, chargement dans synthese_v2.db, jetons et commit d'une extraction v2.
# usage : bash audits/v2/charger_v2.sh PMCID JETONS OUTILS DUREE_S
set -e
cd "$(dirname "$0")/../.."
P=$1
SYNTHESE_DB=synthese_v2.db SYNTHESE_EXTRACT_DIR=extractions_v2 python3 -I load.py check $P | tail -1
SYNTHESE_DB=synthese_v2.db SYNTHESE_EXTRACT_DIR=extractions_v2 python3 -I load.py load $P | tail -1
echo "$P,v2_extraction,sonnet,$2,$3,$4" >> audits/jetons.csv
git add extractions_v2/$P.json audits/jetons.csv
[ -f journaux/${P}_extraction_v2.md ] && git add journaux/${P}_extraction_v2.md
[ -f vocabulaire/ajouts/$P.json ] && git add vocabulaire/ajouts/$P.json
git commit -q -m "v2 : extraction $P

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XpBfw837etGcfE2KpDthTP"
timeout 110 git push origin main 2>&1 | tail -1
