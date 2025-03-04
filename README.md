# MTranServer (Simplified)

> Mini Translation Server Beta Version with
>
> 1. Remove dummy files (the `core` folder is not open sourced yet)
> 2. Add download scripts

Original READMEs: [中文](readme/README_zh.md) | [日本語](readme/README_ja.md) | [English](readme/README_en.md)

## Getting Started

> NOTE: currently no pre-build image for M-series macOS
>
> `no matching manifest for linux/arm64/v8 in the manifest list entries`

## Note

Seems this project use same model as [firefox-translations-models/registry.json](https://github.com/mozilla/firefox-translations-models/blob/250530e63f82e032e2aad483ce23f8b1a7635c08/registry.json#L1419-L1441) / [firefox-translations-models/models/dev/enzh at main · mozilla/firefox-translations-models](https://github.com/mozilla/firefox-translations-models/tree/main/models/dev/enzh)

## Resources

- [OpenNMT/CTranslate2: Fast inference engine for Transformer models](https://github.com/OpenNMT/CTranslate2)
- [mozilla/translations: The code, training pipeline, and models that power Firefox Translations](https://github.com/mozilla/translations)
  - [mozilla/firefox-translations-models: CPU-optimized Neural Machine Translation models for Firefox Translations](https://github.com/mozilla/firefox-translations-models) => Based on browsermt/students?!
- [browsermt/students: Efficient teacher-student models and scripts to make them](https://github.com/browsermt/students) => Based on Marian
  - [students/train-student at master · browsermt/students](https://github.com/browsermt/students/tree/master/train-student)
- [marian-nmt/marian-dev: Fast Neural Machine Translation in C++ - development repository](https://github.com/marian-nmt/marian-dev)
  - [Marian :: Home](https://marian-nmt.github.io/)
