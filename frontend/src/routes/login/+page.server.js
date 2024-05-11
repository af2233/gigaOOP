import { json } from '@sveltejs/kit';
import { BASE_URL } from '../../api.js';

/** @type {import('./$types').Actions} */
export const actions = {
	register: async ({ request }) => {
		const body = await request.formData();
		const name = body.get('name');
		const email = body.get('email');
		const password = body.get('password');

		
		const data = {
			name: name,
			email: email,
			password: password
		};

		const response = await fetch('${BASE_URL}/login', {
			method: 'POST',
			headers: {
			'Content-Type': 'application/json'
			},
			body: JSON.stringify(data)
		});

		// Parse the response from the FastAPI endpoint
		const responseData = await response.json();

		// Return the response from the FastAPI endpoint to the SvelteKit endpoint
		console.log(responseData)
		return {
			message: responseData.message 
		};
	},
	login: async (event) => {
		// login the user
	}
};