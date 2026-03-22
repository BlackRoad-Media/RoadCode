# BlackRoad-Media — RoadCode

> Content & Streaming division of [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc)

Content creation, streaming, and distribution. Self-hosted media pipelines that run on your device, your data, your agents. No platform gatekeepers.

**Domain**: [blackroad.me](https://blackroad.me)

## Products

| Product | What It Does |
|---------|-------------|
| **RoadTube** | Self-hosted video platform — upload, transcode, stream |
| **BlackCast** | Podcast hosting + distribution engine |
| **Media Pipeline** | Automated transcoding, thumbnail generation, CDN distribution |

## Org Hierarchy

```
BlackRoad-OS-Inc (Parent — 254 repos, 67 agents, 7 nodes)
  └── BlackRoad-Media (Content & Streaming)
      ├── RoadCode          ← this repo (workspace + automation)
      ├── operator           ← CLI tools + media scripts
      └── source             ← canonical source tree
```

## Repos in This Org

- [`RoadCode`](https://github.com/BlackRoad-Media/RoadCode) — Workspace hub (this repo)
- [`operator`](https://github.com/BlackRoad-Media/operator) — CLI + media automation
- [`source`](https://github.com/BlackRoad-Media/source) — Source tree for all media products

## Infrastructure

- **Video storage**: MinIO on Cecilia (self-hosted S3-compatible object storage)
- **Transcoding**: FFmpeg pipelines on fleet nodes, Hailo-8 for ML-assisted encoding
- **CDN**: Caddy on Gematria serves 151 domains with Let's Encrypt TLS
- **Streaming**: HLS/DASH adaptive bitrate from local origin servers

## How It Connects

- **Parent**: [BlackRoad-OS-Inc](https://github.com/BlackRoad-OS-Inc) — central coordination
- **Studio**: [BlackRoad-Studio](https://github.com/BlackRoad-Studio) — Video Studio creates, Media distributes
- **Hardware**: [BlackRoad-Hardware](https://github.com/BlackRoad-Hardware) — fleet handles transcoding + storage
- **AI**: [BlackRoad-AI](https://github.com/BlackRoad-AI) — auto-captioning, thumbnail selection, content tagging

## License

Proprietary — BlackRoad OS, Inc. See [LICENSE](./LICENSE).

---

*Remember the Road. Pave Tomorrow.*
