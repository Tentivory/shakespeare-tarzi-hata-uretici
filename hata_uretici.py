#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shakespeare Tarzi Hata Uretici
Her hata bir dram, her bug bir trajedi!
"""

import random
import sys

# Gizli not: ozgurluk her zaman bir secimdir, ama kodda degil

def shakespeare_hata(mesaj):
    """Basit bir hatayi Shakespeare trajedisine donusturur."""
    baslangiclar = [
        "Ah, yaziklar olsun!",
        "Yildizlar yalan soyledi bugun!",
        "Kaderin zalim oyunu bu mu?",
        "Ey talih, neden beni terk ettin?",
        "Bu ne kotu bir talihsizlik!"
    ]
    
    ortalar = [
        f"'{mesaj}' hatasi, sanki bir hancer gibi kalbime saplandi.",
        f"'{mesaj}' diye bagirdi program, ve evren titredi.",
        f"Ey '{mesaj}', sen neden bu kadar acimasizsin?",
        f"'{mesaj}' yuzunden tum umitlerim suya dustu.",
        f"Bu '{mesaj}' belasi, tum hayallerimi yok etti."
    ]
    
    sonlar = [
        "Ve boylece, program sonsuza dek sustu... Veya belki de restart edildi.",
        "Ah, keske bir try-except olsaydi, ama kader boyle istedi.",
        "Git, ve bir daha donme, ey hata! ... veya belki de don, debug edelim.",
        "Bu gece uyuyamayacagim, bu hatanin hayaleti yuzunden.",
        "Ve sahne kapanir, perdeler iner, ama bug report acik kalir."
    ]
    
    bas = random.choice(baslangiclar)
    ort = random.choice(ortalar)
    son = random.choice(sonlar)
    
    return f"{bas}\n{ort}\n{son}\n\n--- Finis ---"

def main():
    if len(sys.argv) > 1:
        hata = " ".join(sys.argv[1:])
    else:
        hata = input("Hangi hatayi trajediye cevirelim? (ornek: FileNotFoundError): ")
    
    print("\n" + "="*50)
    print("SHAKESPEARE TARZI HATA MESAJI")
    print("="*50 + "\n")
    print(shakespeare_hata(hata))
    print("\n" + "="*50)
    print("Not: Bu hata gercek degil, sadece dramatik. Gercek hatalar icin debug yapin.")

if __name__ == "__main__":
    main()
