---
layout: ../layouts/PageLayout.astro
title: "Musik"
description: "Daftar putar musik favorit saya"
---

Di halaman ini, bisa membagikan daftar lagu atau *playlist* musik favorit Anda.

Gunakan tag `{% media audio %}` untuk menyematkan lagu dari platform musik (seperti NetEase atau QQ Music) seperti contoh berikut:

```markdown
{% media audio %}
- title: Playlist Saya
  list:
    - https://music.163.com/#/playlist?id=ID_PLAYLIST_ANDA
{% endmedia %}
```

{% media audio %}
- title: Playlist A
  list:
    - https://music.163.com/#/playlist?id=8676645748
- title: Playlist B
  list:
    - https://music.163.com/#/album?id=358640968
- title: Playlist C
  list:
    - https://music.163.com/playlist?id=7483326429
- title: Playlist D
  list:
    - https://music.163.com/playlist?id=8882890045
{% endmedia %}


