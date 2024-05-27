import { BASE_URL } from '../../api.js';
import { redirect } from '@sveltejs/kit';


/** @type {import('./$types').Actions} */
export const actions = {
	register: async ({ request, cookies }) => {
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
			
			const user = {
				username: email,
				password: password
			};

			// @ts-ignore
			const loginData = new URLSearchParams(user);

			const loginResponse = await fetch(`${BASE_URL}/auth/jwt/login`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/x-www-form-urlencoded'
				},
				body: loginData,
				credentials: 'include' 
			});
		
			if (loginResponse.ok) {
				const setCookieHeader = loginResponse.headers.get('set-cookie');
				if (setCookieHeader) {
					// Устанавливаем куки на сервере, чтобы клиент мог их использовать
					const cookieOptions = parseSetCookieHeader(setCookieHeader);
					cookies.set(cookieOptions.name, cookieOptions.value, cookieOptions.options);
				}
	
				console.log('User logged in successfully');
				throw redirect(303, '/');
			} else {
				let error;
				try {
					error = await loginResponse.json();
				} catch (e) {
					error = { message: 'Unknown error' };
				}
				console.error('Login failed:', error);
				return { success: false, error: error };
			}
		}else if(response.status == 400){
			return {mailAlreadyExists: true}
		}
	},
	login: async ({ request, cookies }) => {
		const body = await request.formData();
		const email = body.get('email');
		const password = body.get('password');

		const user = {
			username: email,
			password: password
		};

		
		// Создаем данные в формате x-www-form-urlencoded
		// @ts-ignore
		const loginData = new URLSearchParams(user);

		const response = await fetch(`${BASE_URL}/auth/jwt/login`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded'
			},
			body: loginData,
			credentials: 'include' 
		});

		if (response.ok) {
			const setCookieHeader = response.headers.get('set-cookie');
            if (setCookieHeader) {
                // Устанавливаем куки на сервере, чтобы клиент мог их использовать
                const cookieOptions = parseSetCookieHeader(setCookieHeader);
                cookies.set(cookieOptions.name, cookieOptions.value, cookieOptions.options);
            }

			console.log('User logged in successfully');
			throw redirect(303, '/');
		} else {
			let error;
			try {
				error = await response.json();
			} catch (e) {
				error = { message: 'Unknown error' };
			}
			console.error('Login failed:', error);
			return { success: false, error: error };
		}
	}
};


function parseSetCookieHeader(setCookieHeader) {
	const parts = setCookieHeader.split(';');
	const [nameValue, ...options] = parts;
	const [name, value] = nameValue.split('=');

	const cookieOptions = options.reduce((acc, option) => {
		const [key, val] = option.trim().split('=');
		if (key.toLowerCase() === 'max-age') {
			acc.expires = new Date(Date.now() + Number(val) * 1000);
		} else {
			acc[key.toLowerCase()] = val || true;
		}
		return acc;
	}, {});

	return {
		name: name.trim(),
		value: value.trim(),
		options: cookieOptions
	};
}