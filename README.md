# 归庭 小说与插图仓库

本仓库管理《归庭》小说文档、独立章节插图和修订记录。游戏实现与外部游戏参考素材不在本仓库中。

最新正文为 `docs/归庭_v07_游戏剧情正文.docx`。v07 用于游戏剧情背书，保留赫铎的两种行动与三个独立结局，具体游戏判定另行设计。现有图片仍在 `art/v05`；适配结果及待调整项见 `art/v07/插图审阅与位置索引.md`，本次没有生成或替换图片。

## 文件结构

- docs：带版本号的DOCX及同版本文字快照。DOCX为评审文档，MD为自动提取的可比较文字，不是另一份改写稿。
- art/v03、art/v04、art/v05：按章节编号保存PNG与位置索引。v03指插图分离版，v04为职业与魔法修订版，v05为伊澜冰系修订版。
- art/v07：v07对应的插图审阅与位置索引，引用v05原图，不重复存储。
- history：修订记录。
- scripts/docx_to_md.py：使用Python标准库提取DOCX中的段落与表格文字。

现有资料从v02带插图整合稿开始归档；这不是全部42条历史聊天原文档案，也不是所有草稿的完整历史。Git提交时间是本次归档时间，不冒充此前的创作时间。

## 版本规则

每次交付使用新版本号，如v05、v06；保留此前的DOCX与插图目录。一个版本完成后提交并创建同名标签。图片与DOCX使用Git LFS；相同内容的图片只存一份LFS对象。

新增纹章、势力标识及专属设定先由作者确认。角色固定：伊澜魔法、陶恩治疗辅助、塞维与赫铎物理；夫妻始终信任。插图编号对应DOCX中的插入位置。

## 本地使用

下载仓库备份ZIP并完整解压，其中包含.git和LFS对象；不需要重新git init。在仓库目录执行：

```bash
git lfs install --local
git status
git log --oneline --decorate
git diff v03 v04 -- docs/
```

新增版本后，提取文字快照并提交：

```bash
python3 scripts/docx_to_md.py docs/归庭_v05.docx docs/归庭_v05.md
git add docs art history
git commit -m "v05：说明本次修改"
git tag v05
```

提交前可在本仓库设置自己的姓名与邮箱。初始归档由“Codex Archive”署名，不冒用作者身份。

## 远程同步

远程仓库：https://github.com/k644606347/gui-ting

正文和图片使用Git LFS。克隆后运行 `git lfs pull` 下载原文件；更新后运行 `git push origin main --follow-tags`。
