#!/usr/bin/env bash
set -euo pipefail

deleted=()

for dir in */*/; do
    declare -A latest=()
    for file in "$dir"submission-*; do
        [ -f "$file" ] || continue
        ext="${file##*.}"
        num="${file##*submission-}"
        num="${num%%.*}"

        if [[ -z "${latest[$ext]+x}" ]] || (( num > latest[$ext] )); then
            latest[$ext]=$num
        fi

    done

    for file in "$dir"submission-*; do
        [ -f "$file" ] || continue
        ext="${file##*.}"
        num="${file##*submission-}"
        num="${num%%.*}"

        if (( num < latest[$ext] )); then
            git rm "$file"
            deleted+=("$file")
        fi

    done

    unset latest
done

if [ ${#deleted[@]} -eq 0 ]; then
    echo "Nothing to clean up"
    exit 0
fi

printf 'Removed: %s\n' "${deleted[@]}"
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"
git commit -m "chore: remove old same-language submissions"
git push
