<script>
    /** @type {import('./$types').PageData} */
    export let data;
</script>


<style>
    section {
        width: 100%;
        height: 100%;
        background-color: #f5f5f5;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
    }
</style>

<section>
    <h1>Course Page</h1>
    <div>
        {#each data.themes as theme}
            <div>{theme.title}</div>
        {/each}
    </div>
</section>
