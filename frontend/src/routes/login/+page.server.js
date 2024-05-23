import { json } from '@sveltejs/kit';
import { BASE_URL } from '../../api.js';

/** @type {import('./$types').Actions} */
export const actions = {
	register: async ({ request }) => {
		const body = await request.formData();
		const email = body.get('email');
		const password = body.get('password');

		
		const user = {
			email: email,
			password: password
		};

		const response = await fetch(`${BASE_URL}/auth/register`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(user)
		});

		if (response.ok) {
			// Обработка успешной регистрации
			console.log('User registered successfully');
		} else if (response.status === 400){
			return { mailAlreadyExists: true }
		}

	},
	login: async (event) => {
		// login the user
	}
};