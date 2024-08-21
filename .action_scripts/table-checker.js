const fs = require('fs');
const readline = require('readline');
const path = require('path');

async function checkMarkdownTable(filename) {
    // 获取脚本所在目录的绝对路径
    const scriptDir = __dirname;
    // 构造目标文件的绝对路径
    const filePath = path.join(scriptDir, '..', filename);

    const fileStream = fs.createReadStream(filePath, 'utf-8');
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let errFlag = 0;
    const uidSet = new Set();
    const idSet = new Set();
    const upSet = new Set();
    const uidUpIdSet = new Set();

    let lineNumber = 0;
    let flag = 0;

    for await (const line of rl) {
        lineNumber++;
        if (lineNumber < 3) continue; // Skip header lines

        const fields = line.trim().split('|');
        if (fields.length < 4) {
            console.error(`异常项：缺少字段（位于第 ${lineNumber} 行）`);
            errFlag = 1;
            continue;
        }

        const [ , uid, up, id ] = fields.map(field => field.trim());

        if (!uid) {
            console.error(`异常项：缺少UID值（位于第 ${lineNumber} 行）`);
            errFlag = 1;
        }
        if (!up) {
            console.error(`异常项：缺少UP值（位于第 ${lineNumber} 行）`);
            errFlag = 1;
        }
        if (!id) {
            console.error(`异常项：缺少ID值（位于第 ${lineNumber} 行）`);
            errFlag = 1;
        }
        if (!uid || !up || !id) continue;

        const uidUpTuple = `${uid},${up},${id}`;
        if (uidUpIdSet.has(uidUpTuple)) {
            console.log(`重复项：UID、UP和ID均相同 - ${uidUpTuple}（位于第 ${lineNumber} 行）`);
            errFlag = 2;
            flag = 1;
        } else {
            uidUpIdSet.add(uidUpTuple);
        }

        if (uidSet.has(uid)) {
            if (flag !== 1) {
                console.warn(`异常项：UID相同但其他值不同 - ${uidUpTuple}（位于第 ${lineNumber} 行）`);
                errFlag = 1;
            }
        }

        if (!/^\d{9}$/.test(uid)) {
            console.error(`异常项：UID格式不正确 - ${uid}（位于第 ${lineNumber} 行）`);
            errFlag = 1;
        } else {
            uidSet.add(uid);
        }

        if (!/^\d+$/.test(id)) {
            console.error(`异常项：ID格式不正确 - ${id}（位于第 ${lineNumber} 行）`);
            errFlag = 1;
        } else {
            idSet.add(id);
        }

        flag = 0;
    }

    console.log("检查完成！");
    return errFlag;
}

const filename = "Search-table.md";
checkMarkdownTable(filename).then(errFlag => process.exit(errFlag)).catch(err => {
    console.error(`错误: ${err.message}`);
    process.exit(3);
});
