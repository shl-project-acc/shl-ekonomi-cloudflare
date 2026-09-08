#!/usr/bin/env python3
"""Audit all blog markdown files for forbidden patterns in headings.

Checks:
1. ZERO colons (:) in frontmatter title or any markdown heading (H1-H6)
2. ZERO occurrences of the word 'Anda' (case-insensitive word boundary)
3. Reports violations with file, line number, and offending text.

Usage:
  python scripts/audit-headings.py <blog_dir>
  # e.g. python scripts/audit-headings.py src/content/blog
"""
import os, re, sys

def audit_blog_dir(blog_dir):
    colon_violations = []
    anda_violations = []
    total_files = 0

    for root, _, files in os.walk(blog_dir):
        for f in files:
            if not f.endswith('.md'):
                continue
            total_files += 1
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                lines = fp.readlines()
            in_fm, fm_count = False, 0
            for idx, line in enumerate(lines, 1):
                stripped = line.strip()
                if stripped == '---':
                    fm_count += 1
                    in_fm = (fm_count == 1)
                    continue
                # Check frontmatter title
                if in_fm and stripped.startswith('title:'):
                    val = stripped[6:].strip()
                    if ':' in val:
                        colon_violations.append((f, idx, 'TITLE', stripped))
                # Check markdown headings
                if stripped.startswith('#'):
                    h_text = re.sub(r'^#+\s*', '', stripped)
                    if ':' in h_text:
                        colon_violations.append((f, idx, 'HEADING', stripped))
            # Check for 'Anda' in full text
            full_text = ''.join(lines)
            for m in re.finditer(r'\bAnda\b', full_text):
                # Find line number
                line_no = full_text[:m.start()].count('\n') + 1
                anda_violations.append((f, line_no, full_text.splitlines()[line_no-1].strip()[:80]))

    print(f'Scanned {total_files} markdown files in {blog_dir}')
    print(f'Colon violations in headings: {len(colon_violations)}')
    for v in colon_violations:
        print(f'  {v[0]} (line {v[1]}) [{v[2]}]: {v[3]}')
    print(f'"Anda" violations: {len(anda_violations)}')
    for v in anda_violations:
        print(f'  {v[0]} (line {v[1]}): {v[2]}')
    if not colon_violations and not anda_violations:
        print('\n✅ ALL CLEAR: 0 colons in headings, 0 "Anda" found.')
        return 0
    else:
        print(f'\n❌ VIOLATIONS FOUND: {len(colon_violations)} colons + {len(anda_violations)} Anda')
        return 1

if __name__ == '__main__':
    blog_dir = sys.argv[1] if len(sys.argv) > 1 else 'src/content/blog'
    sys.exit(audit_blog_dir(blog_dir))
