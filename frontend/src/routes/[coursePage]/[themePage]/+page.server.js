import { marked } from 'marked';
import fs from 'fs/promises';
import path from 'path';
import { error } from '@sveltejs/kit';


/** @type {import('./$types').PageServerLoad} */

export async function load({ params }) {
	const themeId = params.themePage;

	const themeRes = await fetch(`http://localhost:8000/themes/${themeId}`);
	if (!themeRes.ok) {
		throw error(themeRes.status, 'Failed to fetch theme');
	}
	const theme = await themeRes.json();

	const mdPath = path.join(process.cwd(), 'static', 'chapters', `${theme.content}.md`);
	let htmlContent;

	try {
		const markdown = await fs.readFile(mdPath, 'utf8');
		htmlContent = marked(markdown);
	} catch (err) {
		console.error(`File not found: ${mdPath}`, err);
		htmlContent = 'Файл не найден';
	}

	const quizRes = await fetch(`http://localhost:8000/quizzes?theme_id=${themeId}`);
	let quizData = null;

	if (quizRes.ok) {
		const quizzes = await quizRes.json();
		quizData = quizzes.length > 0 ? quizzes[0] : null;
	} else {
		console.warn(`No quiz found for theme ${themeId}`);
	}

	return {
		htmlContent,
		themeTitle: theme.title,
		themeId,
		quizData
	};
}
