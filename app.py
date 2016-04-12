from multithreading import ArticlesParse

urls = ['/wiki/History_of_the_United_States', '/wiki/Ernest_Hemingway', '/wiki/Jupiter', '/wiki/Astronomy_in_medieval_Islam', '/wiki/Radio_astronomy', '/wiki/Tibetan_astronomy', '/wiki/Reionization', '/wiki/Aristarchus_of_Samos', '/wiki/Stellar_nucleosynthesis', '/wiki/Tidal_acceleration', '/wiki/CRC_Press', '/wiki/Hubble_Space_Telescope', '/wiki/Joseph_Louis_Lagrange', '/wiki/Wave', '/wiki/Astrophotography', '/wiki/Gravitational_waves', '/wiki/Sidewalk_astronomy', '/wiki/Encyclopedia_of_the_History_of_Arabic_Science', '/wiki/Interstellar_dust', '/wiki/Volcanism', '/wiki/Observational_astronomy', '/wiki/Near-ultraviolet', '/wiki/Cosmogony', '/wiki/Apparent_magnitude', '/wiki/Chronology_of_the_Universe', '/wiki/Keck_Observatory', '/wiki/Electron', '/wiki/Bremsstrahlung_radiation', '/wiki/Slovakia', '/wiki/Amateur_telescope_making', '/wiki/Natural_satellite', '/wiki/Big_bang', '/wiki/Very_Large_Array', '/wiki/Precession', '/wiki/Planetary_differentiation', '/wiki/Glossary_of_astronomy', '/wiki/Neptune', '/wiki/Population_III_stars', '/wiki/Fine-tuned_universe', '/wiki/Chinese_astronomy', '/wiki/Ja%27far_ibn_Muhammad_Abu_Ma%27shar_al-Balkhi', '/wiki/Gravitation', '/wiki/Gamma-ray_astronomy', '/wiki/Circumstellar_disk', '/wiki/Chambers_Book_of_Days']
print len(urls)
for i, url in enumerate(urls):
    thread = ArticlesParse(i, url)
    thread.start()



print "Exiting Main Thread"

