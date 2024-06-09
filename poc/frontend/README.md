
## Get Started

### Requirements
1.  NodeJS - https://nodejs.org/en/download/package-manager
2.  PNPM - https://pnpm.io/pt/installation

### Install libs
```pnpm run install```

### Build artifact
```pnpm run build```

### Execute Local
```pnpm run dev```

## Running in Container

### Requirements
1.  Navigate to folder "poc"
2.  API - following tutorial <a href="https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/poc/backend">here</a>

### Build image
```docker build -t 'web' -f frontend/Dockerfile .```

### Run image
```docker run -d -p 3000:3000 --name 'web' web```

## Stacks

- Typescript
- React
- PNPM
